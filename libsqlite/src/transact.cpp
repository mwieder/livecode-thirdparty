#include "sqlitedataset.h"

using namespace dbiplus;

int main() {
SqliteDatabase db;
db.setDatabase("profile.sqlite");
Dataset *ds = db.CreateDataset();
db.connect();

   try {
 db.start_transaction();
 ds->exec("create table edge_profiler"
    " (profile_id integer primary key,"
    "  source_pc varchar(9),"
    "  target_pc varchar(9),"
    "  target_samples integer"
    "  )");
 db.commit_transaction();
   } catch (DbErrors &e) {
     std::cerr <<"First catch...\n";
     std::cerr << e.getMsg() << std::endl;
     db.rollback_transaction();
    return -1;
   }

   std::cerr << "table created" << std::endl;

   try {
    db.start_transaction();
    ds->set_autocommit(false);
    ds->open("select source_pc, target_pc, target_samples \n"
    "from edge_profiler");
    ds->add_insert_sql("insert into edge_profiler\n"
        "(source_pc, target_pc, target_samples) values\n"
        "(:NEW_source_pc, :NEW_target_pc, :NEW_target_samples)");
   } catch (DbErrors &e) {
     cerr << "Second catch ...\n";
     db.rollback_transaction();
     std::cerr << e.getMsg() << std::endl;
     return -1;
   }//try

   for (int i=0;  i<10; i++) {
       try {
            std::cout << "No: "<<i <<"\n";
	    ds->insert();
    	    ds->sf("source_pc", "source_pc");
	    ds->sf("target_pc", "target_pc");
	    ds->sf("target_samples", i);
	    ds->post();
	} catch (DbErrors &e) {
	    std::cerr << "Third catch...\n";
	    std::cerr << e.getMsg() << std::endl;
	    db.rollback_transaction();
	    return -1;
        } //try
    } // for
   db.commit_transaction();
   delete ds;
}//main
