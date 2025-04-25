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
} from "@chakra-ui/react";

export default function NewCommuteForm() {
  return (
    <Box>
      <HStack gap="10" width="full">
        <Field.Root required>
          <Field.Label color={"gray"}>
            Commute Name <Field.RequiredIndicator />
          </Field.Label>
          <Input
            placeholder="Work"
            variant="subtle"
            color={"white"}
            backgroundColor={"black"}
          />
        </Field.Root>
        <Field.Root required>
          <Field.Label color={"gray"}>
            Arrival Time <Field.RequiredIndicator />
          </Field.Label>
          <Input
            placeholder="9AM"
            variant="subtle"
            color={"white"}
            backgroundColor={"black"}
          />
        </Field.Root>
      </HStack>
      <HStack gap="10" width="full">
        <Field.Root required>
          <Field.Label color={"gray"}>
            Starting Location <Field.RequiredIndicator />
          </Field.Label>
          <Input
            placeholder="370 Jay Street"
            variant="subtle"
            color={"white"}
            backgroundColor={"black"}
          />
        </Field.Root>
        <Field.Root required>
          <Field.Label color={"gray"}>
            Destination <Field.RequiredIndicator />
          </Field.Label>
          <Input
            placeholder=" 20 W 34th St., New York, 10001"
            variant="subtle"
            color={"white"}
            backgroundColor={"black"}
          />
        </Field.Root>
      </HStack>
      <Text color={"gray"} mt={5}>
        Days Needed
      </Text>
      <HStack align="flex-start" gap={0} mt={5}>
        <For each={["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]}>
          {(day) => (
            <Stack key={day} align="flex-start" flex="1">
              <Checkbox.Root variant={"subtle"}>
                <Checkbox.HiddenInput />
                <HStack>
                  <Text color={"gray"}>{day}</Text>
                  <Checkbox.Control backgroundColor={"black"} color={"white"} />
                  <Checkbox.Label>Checkbox</Checkbox.Label>
                </HStack>
              </Checkbox.Root>
            </Stack>
          )}
        </For>
      </HStack>
      <Flex justifyContent="flex-end" mt={7}>
        <Button
          borderRadius="33.5px"
          backgroundColor={"#6DCD65"}
          _hover={{
            boxShadow: "0 0 20px #6DCD65",
            transform: "scale(1.01)",
            transition: "all 0.3s ease-in-out",
          }}
        >
          Add
        </Button>
      </Flex>
    </Box>
  );
}
