"use client";

import {
    List,
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
                <Table.Column dataIndex="id" title={"ID"} />
                <Table.Column dataIndex="title" title={"title"} />
                <Table.Column
                    title={"Actions"}
                    dataIndex="actions"
                    render={(_, record: BaseRecord) => (
                        <Space>
                            {/* Add your action buttons here */}
                        </Space>
                    )}
                />
            </Table>
        </List>
    );
}