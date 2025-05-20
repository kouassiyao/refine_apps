"use client";

import { NumberField, Show, TextField, DateField } from "@refinedev/antd";
import { useShow, useOne } from "@refinedev/core";
import { Typography } from "antd";

const { Title } = Typography;

export default function BillShow() {
    const { query: queryResult } = useShow({});
    const { data, isLoading } = queryResult;

    const record = data?.data;

    // Fetch vendor details using vendor_id from the bill record
    const { data: vendorData, isLoading: vendorLoading } = useOne({
        resource: "vendors",
        id: record?.vendor_id,
        queryOptions: {
            enabled: !!record?.vendor_id,
        },
    });

    return (
        <Show isLoading={isLoading}>
            <Title level={5}>{"Name"}</Title>
            <TextField value={record?.name} />
            <Title level={5}>{"Issue date"}</Title>
            <DateField value={record?.issue_date} format="YYYY-MM-DD" />
            <Title level={5}>{"Due date"}</Title>
            <DateField value={record?.due_date} format="YYYY-MM-DD" />
            <Title level={5}>{"Amount"}</Title>
            <NumberField value={record?.amount ?? ""} />
            <Title level={5}>{"Vendor"}</Title>
            <TextField value={vendorLoading ? "Loading..." : vendorData?.data?.name} />
        </Show>
    );
}