import {
  Button,
  Card,
  Stack,
  Image,
  Input,
  Field,
  Box,
  HStack,
} from "@chakra-ui/react";
import google from "../assets/google.png";
import { useState } from "react";
import {
  handleSigninWithEmailAndPassword,
  handleCreateUserWithEmailAndPassword,
  handleSignInWithGoogle,
} from "./utils/auth";
// import { useAuth } from "../contexts/auth_context";

export default function LoginForms() {
  // const { userLoggedIn } = useAuth();

  const [formType, setFormType] = useState("none");
  const [formFields, setFormFields] = useState({
    username: "",
    password: "",
    email: "",
  });

  function handleChange(e) {
    const { name, value } = e.target;
    setFormFields((prev) => ({
      ...prev,
      [name]: value,
    }));
  }

  function handeBackBtnClick() {
    setFormType("none");
    setFormFields({
      // Clear all form fields
      username: "",
      password: "",
      email: "",
    });
  }

  return (
    <Card.Body pb={0} w="100%" position="relative" minH="300px">
      {/* Overlapping Form Container */}
      <Box position="relative" w="100%" h="100%">
        {/* Login Options */}
        <Box
          position="absolute"
          top={0}
          left={0}
          w="100%"
          h="100%"
          opacity={formType === "none" ? 1 : 0}
          transform={
            formType === "none" ? "translateY(0px)" : "translateY(-20px)"
          }
          transition="all 0.4s ease-in-out"
        >
          <Stack gap="4">
            <Button
              _hover={{ bg: "#6DCD65", color: "black" }}
              borderRadius="33.5px"
              w="100%"
              borderColor="#6DCD65"
              borderWidth=".5px"
              onClick={() => setFormType("Login")}
            >
              Login
            </Button>
            <Button
              _hover={{ bg: "#6DCD65", color: "black" }}
              borderRadius="33.5px"
              borderColor="#6DCD65"
              borderWidth=".5px"
              onClick={() => setFormType("Signup")}
            >
              Sign up
            </Button>
            <Button
              _hover={{ bg: "#6DCD65", color: "black" }}
              borderRadius="33.5px"
              borderColor="#6DCD65"
              borderWidth=".5px"
              onClick={() => handleSignInWithGoogle()}
            >
              <Image src={google} />
              Sign in with Google
            </Button>
          </Stack>
        </Box>

        {/* Sign up form */}
        <Box
          position="absolute"
          top={0}
          left={0}
          w="100%"
          h="100%"
          opacity={formType === "Signup" ? 1 : 0}
          transform={
            formType === "Signup" ? "translateY(0px)" : "translateY(20px)"
          }
          pointerEvents={formType === "Signup" ? "auto" : "none"}
          transition="all 0.4s ease-in-out"
        >
          <Stack gap="4">
            <Field.Root required>
              <Field.Label>
                Username <Field.RequiredIndicator />
              </Field.Label>
              <Input
                name="username"
                variant="outline"
                bg="rgba(0, 0, 0, 0)"
                borderRadius="8px"
                borderColor="#D1FFCC"
                borderWidth=".5px"
                value={formFields.username}
                onChange={handleChange}
              />
            </Field.Root>
            <Field.Root required>
              <Field.Label>
                Password <Field.RequiredIndicator />
              </Field.Label>
              <Input
                name="password"
                type="password"
                variant="outline"
                value={formFields.password}
                onChange={handleChange}
                bg="rgba(0, 0, 0, 0)"
                borderRadius="8px"
                borderColor="#D1FFCC"
                borderWidth=".5px"
              />
            </Field.Root>
            <Field.Root required>
              <Field.Label>
                Email <Field.RequiredIndicator />
              </Field.Label>
              <Input
                name="email"
                variant="outline"
                type="email"
                bg="rgba(0, 0, 0, 0)"
                borderRadius="8px"
                borderColor="#D1FFCC"
                borderWidth=".5px"
                value={formFields.email}
                onChange={handleChange}
              />
            </Field.Root>
            <HStack justify={"center"}>
              <Button
                borderRadius="33.5px"
                borderColor="#6DCD65"
                borderWidth=".5px"
                mt={2}
                onClick={() => handleCreateUserWithEmailAndPassword(formFields)}
                w={100}
                _hover={{ bg: "#6DCD65", color: "black" }}
              >
                Signup
              </Button>
              <Button
                _hover={{ bg: "#6DCD65", color: "black" }}
                borderRadius="33.5px"
                borderColor="#6DCD65"
                borderWidth=".5px"
                mt={2}
                w={100}
                onClick={handeBackBtnClick}
              >
                Back
              </Button>
            </HStack>
          </Stack>
        </Box>
        {/* Login form */}
        <Box
          position="absolute"
          top={0}
          left={0}
          w="100%"
          h="100%"
          opacity={formType === "Login" ? 1 : 0}
          transform={
            formType === "Login" ? "translateY(0px)" : "translateY(20px)"
          }
          pointerEvents={formType === "Login" ? "auto" : "none"}
          transition="all 0.4s ease-in-out"
        >
          <Stack gap="4">
            <Field.Root required>
              <Field.Label>
                Username <Field.RequiredIndicator />
              </Field.Label>
              <Input
                name="username"
                variant="outline"
                bg="rgba(0, 0, 0, 0)"
                borderRadius="8px"
                borderColor="#D1FFCC"
                borderWidth=".5px"
                value={formFields.username}
                onChange={handleChange}
              />
            </Field.Root>
            <Field.Root required>
              <Field.Label>
                Password <Field.RequiredIndicator />
              </Field.Label>
              <Input
                name="password"
                variant="outline"
                type="password"
                bg="rgba(0, 0, 0, 0)"
                borderRadius="8px"
                borderColor="#D1FFCC"
                borderWidth=".5px"
                value={formFields.password}
                onChange={handleChange}
              />
            </Field.Root>

            <HStack justify={"center"}>
              <Button
                borderRadius="33.5px"
                borderColor="#6DCD65"
                borderWidth=".5px"
                mt={2}
                onClick={() => handleLogin(formFields)}
                w={100}
                _hover={{ bg: "#6DCD65", color: "black" }}
              >
                Login
              </Button>
              <Button
                _hover={{ bg: "#6DCD65", color: "black" }}
                borderRadius="33.5px"
                borderColor="#6DCD65"
                borderWidth=".5px"
                mt={2}
                w={100}
                onClick={handeBackBtnClick}
              >
                Back
              </Button>
            </HStack>
          </Stack>
        </Box>
      </Box>
    </Card.Body>
  );
}
