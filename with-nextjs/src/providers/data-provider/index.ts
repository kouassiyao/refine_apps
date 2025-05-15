"use client";

import dataProviderSimpleRest from "@refinedev/simple-rest";

const API_URL = "https://api.fake-rest.refine.dev";

export const dataProvider = dataProviderSimpleRest(API_URL);
export const billsDataProvider = dataProviderSimpleRest(`${BILLS_API_URL}`);