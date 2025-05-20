"use client";

import { NumberField, Show, TextField } from "@refinedev/antd";
import { useShow } from "@refinedev/core";
import { Typography } from "antd";

const { Title } = Typography;

export default function BillShow() {
    const { query: queryResult } = useShow({});
    const { data, isLoading } = queryResult;

    const record = data?.data;

    return (
        <Show isLoading={isLoading}>
            <Title level={5}>{"ID"}</Title>
            <TextField value={record?.id} />
            <Title level={5}>{"Name"}</Title>
            <TextField value={record?.name} />
            <Title level={5}>{"Issue date"}</Title>
            <TextField value={record?.issue_date} />
            <Title level={5}>{"Due date"}</Title>
            <TextField value={record?.due_date} />
            <Title level={5}>{"Amount"}</Title>
            <NumberField value={record?.amount ?? ""} />
        </Show>
    );
}