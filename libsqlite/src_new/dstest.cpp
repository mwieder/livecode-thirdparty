/**********************************************************************
 * Copyright (c) 2004, Leo Seib, Hannover
 *
 * Project:Dataset C++ Dynamic Library
 * Module: SQLiteDataset use example file
 * Author: Leo Seib      E-Mail: leoseib@web.de
 * Begin: 5/04/2002
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 **********************************************************************/

#include "sqlitedataset.h"
#include <memory>
using namespace dbiplus;

int main(){

  // Variables declaration and connection to database
   SqliteDatabase db;
   db.setDatabase("test.db");
   auto_ptr<Dataset> ds(db.CreateDataset());
   db.connect();

   cout << "Querying database schema:\n\n";

  try { 
  ds->query(" select * from sqlite_master");
  } catch (DbErrors &e ) {
    cout << "\n"<<e.getMsg()<<"\n";
  }
  cout << "Num rows:"<<ds->num_rows()<<"\n";
  cout <<"____________________________________________\n\n";

  //Query result navigation
  //ds->first();
  cout <<"Query result navigation:\n";
  cout <<"From first to last:\n";
  while (!ds->eof()) {
    cout << ds->fv("type")<<"|"<<ds->fv("name")<<"\n";
    ds->next();
  }

  cout <<"____________________________________________\n\n";

  cout <<"From last to first:\n";
  ds->last();
  while (!ds->bof()) {
    cout << ds->fv("type")<<"|"<<ds->fv("name")<<"\n";
    ds->prev();
  }

  cout <<"____________________________________________\n\n";

  cout <<"Using seek function:\n";
  ds->seek(1);
  while (!ds->eof()) {
    cout << ds->fv("type")<<"|"<<ds->fv("name")<<"\n";
    ds->next();
  }

  cout <<"____________________________________________\n\n";
  cout <<"Using goto_rec function:\n";
  ds->goto_rec(1);
  while (!ds->eof()) {
    cout << ds->fv("type")<<"|"<<ds->fv("name")<<"\n";
    ds->next();
  }


  cout <<"____________________________________________\n\n";


  //Create db_sequence table for nextid() function
  ds->query("select * from sqlite_master where type like 'table' and name like 'db_sequence'");
  if (ds->num_rows() == 0) {
      cout << "Creating db_sequence table\n";
    ds->exec("create table db_sequence (seq_name verchar(32) primary key, nextid integer)");
    cout <<"Ok!\n";
  }
  
  cout <<"____________________________________________\n\n";
  cout <<"Using nextid function (table db_sequence(nextid int,seq_name varchar(32) primary key) MUST exist!)\n\n";

  cout << "Nextid:"<<ds->nextid("seq1")<<"\n";


  cout <<"____________________________________________\n\n";

  //Create sample table
  try {
    db.start_transaction();
    ds->query("select * from sqlite_master where type like 'table' and name like 'employers'");
    if (ds->num_rows()==0) {
      cout << "Creating sample tables\n";
      ds->exec("create table employers (id integer primary key,firstname varchar(32), name varchar (32))");
      ds->exec("create table address (id integer primary key, ownerid integer, street varchar(64),zip varchar(12),town varchar(64),country varchar(64))");
      ds->exec("create index oid on address (ownerid)");
      cout << "Ok!\n\n";
    }
    db.commit_transaction();
  }
  catch (...) { db.rollback_transaction(); }

try {
   ds->set_select_sql("select a.id as bid,a.firstname,a.name,b.id as aid,b.ownerid as oid,b.street,b.zip,b.town,b.country from employers a, address b where a.id = b.ownerid");
   ds->add_update_sql("update employers set name=:NEW_name,firstname=:NEW_firstname where id=:OLD_bid");
   ds->add_update_sql("update address set street=:NEW_street,zip=:NEW_zip,town=:NEW_town,country=:NEW_country  where id=:OLD_aid");
   ds->add_insert_sql("insert into employers (id,name,firstname) values (:NEW_bid,:NEW_name,:NEW_firstname)");
   ds->add_insert_sql("insert into address (id,ownerid,street,zip,town,country) values (:NEW_aid,:NEW_bid,:NEW_street,:NEW_zip,:NEW_town,:NEW_country)");
   ds->add_delete_sql("delete from employers where id=:OLD_bid");
   ds->add_delete_sql("delete from address where id=:OLD_aid");


   //Opening with defined select sql

  cout <<"Opening Employers and Address database query:\n";
  ds->open();
   //ds->first();
  cout << "Results:\n";
  while (!ds->eof()) {
     cout << ds->fv("name")<<"|"<<ds->fv("bid")<<"\n";
     ds->next();
   }

   //inserting new values into tables (employers and address)
  cout <<"\n\nInserting new values into Employers and Address tables\n";
   db.start_transaction();
   ds->insert();
   field_value fv;
   ds->sf("bid",fv=ds->nextid("e"));
   ds->sf("oid",fv);
   ds->sf("aid",ds->nextid("a"));
   ds->sf("name","name1");
   ds->sf("firstname","firstname1");
   ds->sf("street","street1");
   ds->sf("zip","zip1");
   ds->sf("town","town1");
   ds->sf("country","country1");
   ds->post();
   db.commit_transaction();
   cout <<"Ok!\n\n";
  cout <<"New datas:\n";
  ds->first();
  while (!ds->eof()) {
     cout << ds->fv("name")<<"|"<<ds->fv("bid")<<"\n";
     ds->next();
   }
 
   cout << "\n\nEditing value of last record\n";
   db.start_transaction();
   ds->edit();
   ds->sf("aid",ds->nextid("a"));
   ds->sf("name","name1 changed");
   ds->sf("firstname","firstname1 changed");
   ds->sf("street","street1 changed");
   ds->sf("zip","zip1 changed");
   ds->sf("town","town1 changed");
   ds->sf("country","country1 changed");
   ds->post();
   db.commit_transaction();   
   cout << "Ok!\n\n";

  cout <<"Changed datas:\n";
  ds->first();
  while (!ds->eof()) {
     cout << ds->fv("name")<<"|"<<ds->fv("bid")<<"\n";
     ds->next();
   }

   cout <<"\n\nUsing exec function with result set\n\n";
   ds->exec("select * from sqlite_master");
   result_set* r = (result_set*)ds->getExecRes();
   int i,j;
   for (i = 0; i < r->record_header.size(); i++)
     cout <<r->record_header[i].name<<"|";
   cout <<"\n_________________________________________________________________________\n";
   for (i = 0; i < r->records.size(); i++) {
     for (j = 0; j < r->records[i].size(); j++)
       cout <<r->records[i][j]<<"|";
     cout <<"\n";
   }

  } catch (DbErrors &e ) {
  cout << "Error "<<e.getMsg()<<"\n";
  }
    
}
