import { Card, Center, Text, Image, HStack } from "@chakra-ui/react";
import logoGreen from "../assets/logo-green.png";
import LoginForms from "./login-forms";
export default function LoginBox() {
  return (
    <Card.Root
      minW={"400px"}
      color={"white"}
      pt={75}
      pb={50}
      borderRadius="33.5px"
      bg="rgba(0, 0, 0, 0.05)" // dark translucent background
      backdropFilter="blur(50px)" // this gives the frosted glass effect
      border="1px solid rgba(255, 255, 255, 0.1)" // optional subtle border
    >
      <Card.Header pt={5} pb={11}>
        <Center>
          <Card.Title>
            <HStack>
              <Image src={logoGreen} alt="subway graphic" />
              <Text mt={2} textStyle="2xl">
                Daily Commuter
              </Text>
            </HStack>
          </Card.Title>
        </Center>
      </Card.Header>
      {/* LOGIN MAIN MENU */}
      <LoginForms />
    </Card.Root>
  );
}
