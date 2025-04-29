import {
  Box,
  Field,
  HStack,
  Text,
  FieldLabel,
  FieldRoot,
  Icon,
  Accordion,
  Span,
  Stack,
} from "@chakra-ui/react";
import { FaArrowRight } from "react-icons/fa6";
// placeholder records
const items = [
  {
    value: "a",
    title: "Work",
    arrivalTime: "9:00 AM",
    startingLocation: "333 Water St",
    destination: "123 Madison Ave",
    days: ["Mon", "Tue", "Wed", "Thu"],
    stringDays: "Mon, Tue, Wed, Thu",
  },
  {
    value: "b",
    title: "School Pickup",
    arrivalTime: "3:00 PM",
    startingLocation: "333 Water St",
    destination: "Lincoln Elementary",
    days: ["Thu", "Fri"],
    stringDays: "Thu, Fri",
  },
  {
    value: "c",
    title: "Doc Appointment",
    arrivalTime: "2:30 PM",
    startingLocation: "333 Water St",
    destination: "456 Union Sq",
    days: ["Sun"],
    stringDays: "Sun",
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
              <Stack>
                <Span flex="1" color={"white"}>
                  {item.title}
                </Span>
              </Stack>

              <Accordion.ItemIndicator />
            </Accordion.ItemTrigger>
            <Accordion.ItemContent>
              <Accordion.ItemBody color={"white"}>
                <HStack gap={10}>
                  <Stack>
                    <Field.Root>
                      <Field.Label color={"gray"}>
                        Arrival Time: <Field.RequiredIndicator />
                      </Field.Label>
                    </Field.Root>
                    {item.arrivalTime}
                  </Stack>

                  <Stack>
                    <Field.Root>
                      <Field.Label color={"gray"}>
                        Starting Location: <Field.RequiredIndicator />{" "}
                      </Field.Label>
                    </Field.Root>
                    <HStack>
                      {item.startingLocation}
                      <Icon name="arrow-forward" size="64px">
                        <FaArrowRight />
                      </Icon>
                    </HStack>
                  </Stack>

                  <Stack>
                    <Field.Root>
                      <Field.Label color={"gray"}>
                        Destination: <Field.RequiredIndicator />
                      </Field.Label>
                    </Field.Root>
                    {item.destination}
                  </Stack>

                  <Stack>
                    <Field.Root>
                      <Field.Label color={"gray"}>
                        Days Needed <Field.RequiredIndicator />
                      </Field.Label>
                    </Field.Root>
                    {item.stringDays}
                  </Stack>
                </HStack>
              </Accordion.ItemBody>
            </Accordion.ItemContent>
          </Accordion.Item>
        ))}
      </Accordion.Root>
    </Box>
  );
}
