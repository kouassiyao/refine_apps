"use client";

import { Edit, useForm } from "@refinedev/antd";
import { Form, Input, DatePicker } from "antd";
import dayjs from "dayjs";

export default function BillEdit() {
    const { formProps, saveButtonProps, query: queryResult } = useForm();

    return (
        <Edit saveButtonProps={saveButtonProps}>
            <Form {...formProps} layout="vertical">
                <Form.Item
                    label={"Name"}
                    name={["name"]}
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input />
                </Form.Item>
                <Form.Item
                    label={"Issue date"}
                    name="issue_date"
                    getValueProps={(value) => ({
                        value: value ? dayjs(value) : null,
                    })}
                    getValueFromEvent={(date) => (date ? date.format("YYYY-MM-DD") : null)}
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <DatePicker />
                </Form.Item>
                <Form.Item
                    label={"Due date"}
                    name="due_date"
                    getValueProps={(value) => ({
                        value: value ? dayjs(value) : null,
                    })}
                    getValueFromEvent={(date) => (date ? date.format("YYYY-MM-DD") : null)}
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <DatePicker />
                </Form.Item>
                <Form.Item
                    label={"Amount"}
                    name="amount"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input />
                </Form.Item>
            </Form>
        </Edit>
    );
}