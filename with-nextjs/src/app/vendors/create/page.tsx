"use client";

import { Create, useForm } from "@refinedev/antd";
import { Form, Input } from "antd";

export default function BillCreate() {
    const { formProps, saveButtonProps } = useForm({});

    return (
        <Create saveButtonProps={saveButtonProps}>
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
                    label={"VAT"}
                    name={["vat_number"]}
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Input />
                </Form.Item>
            </Form>
        </Create>
    )
}