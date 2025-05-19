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
import { useState } from "react";
import { addCommuteToDB } from "./utils/db-calls";

export default function NewCommuteForm() {
  const [formFields, setFormFields] = useState({
    commuteName: "",
    startingLocation: "",
    arrivalTime: "",
    destination: "",
    daysNeeded: [],
  });

  function handleChange(e) {
    const { name, value } = e.target;
    setFormFields((prev) => ({
      ...prev,
      [name]: value,
    }));
  }

  function handleDayToggle(day) {
    setFormFields((prev) => {
      const isSelected = prev.daysNeeded.includes(day);
      return {
        ...prev,
        daysNeeded: isSelected
          ? prev.daysNeeded.filter((d) => d !== day) // if already selected, remove it
          : [...prev.daysNeeded, day], // otherwise, add it
      };
    });
  }

  return (
    <Box>
      <HStack gap="10" width="full" mt={5}>
        <Field.Root required>
          <Field.Label color={"gray"}>
            Commute Name <Field.RequiredIndicator />
          </Field.Label>
          <Input
            placeholder="Work"
            variant="subtle"
            color={"white"}
            backgroundColor={"#181818"}
            name="commuteName"
            value={formFields.commuteName}
            onChange={handleChange}
            fontSize={"lg"}
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
            backgroundColor={"#181818"}
            name="arrivalTime"
            value={formFields.arrivalTime}
            onChange={handleChange}
            fontSize={"lg"}
          />
        </Field.Root>
      </HStack>
      <HStack gap="10" width="full" mt={5}>
        <Field.Root required>
          <Field.Label color={"gray"}>
            Starting Location <Field.RequiredIndicator />
          </Field.Label>
          <Input
            placeholder="370 Jay Street"
            variant="subtle"
            color={"white"}
            backgroundColor={"#181818"}
            name="startingLocation"
            value={formFields.startingLocation}
            onChange={handleChange}
            fontSize={"lg"}
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
            backgroundColor={"#181818"}
            name="destination"
            value={formFields.destination}
            onChange={handleChange}
            fontSize={"lg"}
          />
        </Field.Root>
      </HStack>
      <Field.Root required mt={5}>
        <Field.Label color={"gray"}>
          Days Needed <Field.RequiredIndicator />
        </Field.Label>
      </Field.Root>
      <HStack mt={5} gap={7}>
        <For each={["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]}>
          {(day) => (
            <Stack key={day}>
              <Checkbox.Root
                variant={"solid"}
                checked={formFields.daysNeeded.includes(day)}
                onCheckedChange={() => handleDayToggle(day)}
              >
                <Checkbox.HiddenInput />
                <HStack>
                  <Checkbox.Control />
                  <Checkbox.Label color={"gray"}>{day}</Checkbox.Label>
                </HStack>
              </Checkbox.Root>
            </Stack>
          )}
        </For>

        <Button
          ml="auto"
          borderRadius="33.5px"
          backgroundColor={"#6DCD65"}
          _hover={{
            boxShadow: "0 0 20px #6DCD65",
            transform: "scale(1.01)",
            transition: "all 0.3s ease-in-out",
          }}
          onClick={() => addCommuteToDB(formFields)}
        >
          Add
        </Button>
      </HStack>
    </Box>
  );
}
