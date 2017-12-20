// Copyright (c) 2017 The Chromium Embedded Framework Authors. All rights
// reserved. Use of this source code is governed by a BSD-style license that
// can be found in the LICENSE file.
//
// ---------------------------------------------------------------------------
//
// This file was generated by the CEF translator tool. If making changes by
// hand only do so within the body of existing method and function
// implementations. See the translator.README.txt file in the tools directory
// for more information.
//
// $hash=843899ae8ed15cf957ab8289ee917d48c1b2080f$
//

#include "libcef_dll/cpptoc/set_cookie_callback_cpptoc.h"

namespace {

// MEMBER FUNCTIONS - Body may be edited by hand.

void CEF_CALLBACK
set_cookie_callback_on_complete(struct _cef_set_cookie_callback_t* self,
                                int success) {
  // AUTO-GENERATED CONTENT - DELETE THIS COMMENT BEFORE MODIFYING

  DCHECK(self);
  if (!self)
    return;

  // Execute
  CefSetCookieCallbackCppToC::Get(self)->OnComplete(success ? true : false);
}

}  // namespace

// CONSTRUCTOR - Do not edit by hand.

CefSetCookieCallbackCppToC::CefSetCookieCallbackCppToC() {
  GetStruct()->on_complete = set_cookie_callback_on_complete;
}

template <>
CefRefPtr<CefSetCookieCallback> CefCppToCRefCounted<
    CefSetCookieCallbackCppToC,
    CefSetCookieCallback,
    cef_set_cookie_callback_t>::UnwrapDerived(CefWrapperType type,
                                              cef_set_cookie_callback_t* s) {
  NOTREACHED() << "Unexpected class type: " << type;
  return NULL;
}

#if DCHECK_IS_ON()
template <>
base::AtomicRefCount CefCppToCRefCounted<CefSetCookieCallbackCppToC,
                                         CefSetCookieCallback,
                                         cef_set_cookie_callback_t>::DebugObjCt
    ATOMIC_DECLARATION;
#endif

template <>
CefWrapperType CefCppToCRefCounted<CefSetCookieCallbackCppToC,
                                   CefSetCookieCallback,
                                   cef_set_cookie_callback_t>::kWrapperType =
    WT_SET_COOKIE_CALLBACK;
