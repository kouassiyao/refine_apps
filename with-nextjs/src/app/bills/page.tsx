"use client";

import {
    List,
    ShowButton,
    EditButton,
    DeleteButton,
    useTable,
} from "@refinedev/antd";
import type { BaseRecord } from "@refinedev/core";
import { Space, Table } from "antd";

export default function BillList() {
    const { tableProps } = useTable({
        syncWithLocation: true,
    });

    return (
        <List>
            <Table {...tableProps} rowKey="id">
                <Table.Column dataIndex="name" title={"Name"} />
                <Table.Column dataIndex="issue_date" title={"Issue date"} />
                <Table.Column dataIndex="due_date" title={"Due date"} />
                <Table.Column dataIndex="amount" title={"Amount"} />
                {/* <Table.Column dataIndex="vendor_id" title={"vendor identifier"} /> */}
                <Table.Column
                    title={"Actions"}
                    dataIndex="actions"
                    render={(_, record: BaseRecord) => (
                        <Space>
                            <ShowButton hideText size="small" recordItemId={record.id} />
                            <EditButton hideText size="small" recordItemId={record.id} />
                            <DeleteButton hideText size="small" recordItemId={record.id} />
                        </Space>
                    )}
                />
            </Table>
        </List>
    );
}