"use client";

import { Create, useForm, useSelect } from "@refinedev/antd";
import { Form, Input, Select, DatePicker } from "antd";
import dayjs from "dayjs";

export default function BillCreate() {
    const { formProps, saveButtonProps } = useForm({});

    const { selectProps: vendorSelectProps } = useSelect({
        resource: "vendors", // Make sure this matches your resource name in the data provider
        optionLabel: "name", // The field to display
        optionValue: "id",   // The field to use as value
    });

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
                    <Input type="number" />
                </Form.Item>
                <Form.Item
                    label={"Vendor"}
                    name="vendor_id"
                    rules={[
                        {
                            required: true,
                        },
                    ]}
                >
                    <Select
                        showSearch
                        allowClear
                        placeholder="Select a vendor"
                        filterOption={(input, option) =>
                            (option?.label ?? "").toLowerCase().includes(input.toLowerCase())
                        }
                        {...vendorSelectProps}
                    />
                </Form.Item>
                <Form.Item
                    label={"Status"}
                    name={["status"]}
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