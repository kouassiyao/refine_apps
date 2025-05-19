"use client";

import dataProviderSimpleRest from "@refinedev/simple-rest";

const API_URL = "https://api.fake-rest.refine.dev";

export const dataProvider = dataProviderSimpleRest(API_URL);

// Use environment variable for the Bills API URL (set NEXT_PUBLIC_BILLS_API_URL in your .env.local file)
const TRANSACTIONS_API_URL = process.env.NEXT_PUBLIC_TRANSACTIONS_API_URL!;
export const transactionsApiDataProvider = dataProviderSimpleRest(TRANSACTIONS_API_URL);