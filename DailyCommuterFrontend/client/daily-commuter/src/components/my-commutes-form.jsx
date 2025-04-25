import {
  Box,
  Field,
  HStack,
  Input,
  Checkbox,
  For,
  Stack,
  Text,
  Button,
  Flex,
  Accordion,
  Span,
} from "@chakra-ui/react";

const items = [
  { value: "a", title: "Work", text: "Arrive at 9:00 AM, 123 Madison Ave" },
  {
    value: "b",
    title: "School Pickup",
    text: "Pickup at 3:00 PM, Lincoln Elementary",
  },
  {
    value: "c",
    title: "Doc Appointment",
    text: "Appointment at 2:30 PM, 456 Union Sq",
  },
];
export default function MyCommutesForm() {
  return (
    <Box>
      <HStack>
        <Text color={"white"}> Commutes: </Text>
        <Text color={"blue.500"}> 3</Text>
      </HStack>

      <Accordion.Root collapsible defaultValue={["b"]}>
        {items.map((item, index) => (
          <Accordion.Item key={index} value={item.value}>
            <Accordion.ItemTrigger>
              <Span flex="1" color={"white"}>
                {item.title}
              </Span>
              <Accordion.ItemIndicator />
            </Accordion.ItemTrigger>
            <Accordion.ItemContent>
              <Accordion.ItemBody color={"white"}>
                {item.text}
              </Accordion.ItemBody>
            </Accordion.ItemContent>
          </Accordion.Item>
        ))}
      </Accordion.Root>
    </Box>
  );
}
