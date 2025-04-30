import {
  Box,
  Card,
  Stack,
  Center,
  Text,
  Separator,
  Accordion,
  Span,
  Button,
  HStack,
  Icon,
} from "@chakra-ui/react";
import background from "../assets/background.png";
import { useState, useEffect } from "react";
import { FaHouse } from "react-icons/fa6";
import { Link as ChakraLink } from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";

export default function CommutingPage() {
  const items = [
    {
      value: "a",
      title:
        "Walk to 59th Street station and take the 4 train towards Woodlawn",
      text: "<LoremIpsum /> ",
    },
    { value: "b", title: "Take 4 to 14th Street", text: "<LoremIpsum />" },
    { value: "c", title: "Change to the L", text: "<LoremIpsum />" },
    {
      value: "d",
      title: "Take the L to Knickerbocker Ave",
      text: "<LoremIpsum />",
    },
  ];
  const [openItem, setOpenItem] = useState(null);

  useEffect(() => {
    if (!openItem && items.length > 0) {
      setOpenItem(items[0].value);
    }
  }, [openItem, items]);

  const handleNext = (currentValue) => {
    const currentIndex = items.findIndex((item) => item.value === currentValue);
    const nextItem = items[currentIndex + 1];
    if (nextItem) {
      setOpenItem(nextItem.value);
    }
  };

  return (
    <Box
      bgImage={`url(${background})`}
      bgRepeat="no-repeat"
      bgSize="cover"
      bgPosition="center"
      bgAttachment="fixed"
      minHeight="100vh"
      position="relative"
      overflow="hidden"
    >
      <Center>
        <Stack gap="4" direction="row" wrap="wrap">
          <Card.Root
            mt={10}
            bg={"#161616"}
            borderColor={"gray"}
            borderRadius="33.5px"
            minWidth="90vw"
          >
            <Card.Body gap="2">
              <HStack>
                <Text fontSize={"xl"} color={"white"}>
                  Work
                </Text>
                <ChakraLink as={RouterLink} to="/home" ml="auto">
                  <Button
                    backgroundColor={"#373636"}
                    _hover={{
                      transform: "scale(1.08)",
                      transition: "all 0.3s ease-in-out",
                    }}
                  >
                    <Icon>
                      <FaHouse size="28px" />
                    </Icon>
                  </Button>
                </ChakraLink>
              </HStack>

              <Separator color={"gray"} mt={5} opacity={0.5} />
              <Accordion.Root
                spaceY="3"
                variant="plain"
                collapsible
                value={openItem ? [openItem] : []}
                onValueChange={(val) => setOpenItem(val[0] || null)}
              >
                {items.map((item, index) => {
                  const stylingTernary = openItem === item.value;

                  return (
                    <Accordion.Item key={index} value={item.value}>
                      <Box position="relative">
                        {/* Don't use Accordion.ItemTrigger here to prevent row click */}
                        <Box
                          display="flex"
                          alignItems="center"
                          justifyContent="space-between"
                          p={1}
                          borderRadius="md"
                        >
                          <Span
                            flex="1"
                            color={openItem === item.value ? "white" : "gray"}
                            fontSize={openItem === item.value ? "lg" : "md"}
                            transition="all 0.3s ease-in-out"
                          >
                            {item.title}
                          </Span>
                          <Button
                            variant="subtle"
                            colorPalette="blue"
                            onClick={
                              () =>
                                openItem === item.value
                                  ? handleNext(item.value) // "Next" → go forward
                                  : setOpenItem(item.value) // "Skip to this step" → go directly
                            }
                            backgroundColor={
                              stylingTernary ? "#0075F5" : "#373636"
                            }
                            color={"white"}
                            transition="all 0.3s ease-in-out"
                            borderRadius="33.5px"
                            w={150}
                            alignSelf="center"
                            display="flex"
                            alignItems="center"
                            justifyContent="center"
                          >
                            {stylingTernary ? "Next" : "skip to this step"}
                          </Button>
                        </Box>
                      </Box>
                      <Separator color={"gray"} opacity={0.5} />
                      {/* 
        <Accordion.ItemContent>
          <Accordion.ItemBody>{item.text}</Accordion.ItemBody>
          // more data could be added here 
        </Accordion.ItemContent> 
      */}
                    </Accordion.Item>
                  );
                })}
              </Accordion.Root>
            </Card.Body>
          </Card.Root>
        </Stack>
      </Center>
    </Box>
  );
}
