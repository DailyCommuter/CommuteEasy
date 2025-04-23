import { Box, Text, Flex, Button, Image, Center } from "@chakra-ui/react";
import background from "../assets/background.png";
import arrowLogo from "../assets/arrow.svg";
import subwayGraphic from "../assets/subway-graphic.png";
import LoginBox from "../components/login-box";
import { useState } from "react";
import {motion} from "framer-motion";

export default function WelcomePage() {
  const [loginMenu, setLoginMenu] = useState(false);

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
      <Image
        src={subwayGraphic}
        alt="subway graphic"
        position="absolute"
        top="0"
        left="60%"
        transform="translateX(-50%)"
        zIndex="10"
        pointerEvents="none"
        w="80%"
      />

      <Box
        position="relative"
        width="100%"
        height="100vh"
        display="flex"
        alignItems="center"
        justifyContent="center"
      >
        {/* Animate Welcome Content / Tex */}
        <motion.div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              justifyContent: "center",
              position: "absolute",
            }}


          initial = {{opacity: 0, y:20}}
          animate = {{opacity: 1, y:0}}
          transition =  {{duration: 1, delay:0.3}} //disolve / smoothdelay
        >       
        {/* Intro content */}
        <Flex
          direction="column"
          align="center"
          justify="center"
          position="absolute"
          transition="all 0.4s ease-in-out"
          opacity={loginMenu ? 0 : 1}
          transform={loginMenu ? "translateY(-20px)" : "translateY(0px)"}
        >
          <Text
            textStyle="7xl"
            color="white"
            fontWeight="bold"
            textAlign="center"
          >
            Daily
          </Text>
          <Text
            textStyle="7xl"
            color="white"
            fontWeight="bold"
            textAlign="center"
          >
            Commuter
          </Text>
          <Center justifyContent={"center"}>
            <Button
              size="lg"
              mt="10"
              color="black"
              backgroundColor="#6DCD65"
              borderRadius="33.5px"
              onClick={() => setLoginMenu(true)}
              _hover={{
                boxShadow:"0 0 20px #6DCD65",
                transform:"scale(1.01)",
                transition: "all 0.3s ease-in-out",
              }}
            >
              Never Late Again
            </Button>
            <Image 
              src={arrowLogo} 
              alt="subway graphic" 
              mt="10"
              onClick={() => setLoginMenu(true)}s
              _hover={{
                filter: "drop-shadow(0 0 10px white)",
                transform: "scale(1.05)",
                transition: "all 0.3s ease-in-out",
              }}
            />
          </Center>
        </Flex>
        </motion.div> 

        {/* Login Box */}
        <Box
          position="absolute"
          transition="all 0.4s ease-in-out"
          opacity={loginMenu ? 1 : 0}
          transform={loginMenu ? "translateY(0px)" : "translateY(20px)"}
          pointerEvents={loginMenu ? "auto" : "none"}
        >
          <LoginBox setLoginMenu={setLoginMenu} />
        </Box>
      </Box>
    </Box>
  );
}
