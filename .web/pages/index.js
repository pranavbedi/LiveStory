/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useEffect, useState } from "react"
import { ColorModeContext, EventLoopContext } from "/utils/context"
import { Event, getBackendURL, isTrue, refs } from "/utils/state"
import { MoonIcon as LucideMoonIcon, SunIcon as LucideSunIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { toast, Toaster } from "sonner"
import env from "/env.json"
import { Button as RadixThemesButton, Code as RadixThemesCode, Container as RadixThemesContainer, Flex as RadixThemesFlex, Heading as RadixThemesHeading, IconButton as RadixThemesIconButton, Link as RadixThemesLink, Text as RadixThemesText } from "@radix-ui/themes"
import NextLink from "next/link"
import NextHead from "next/head"



export function Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d () {
  const { resolvedColorMode } = useContext(ColorModeContext)


  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const toast_props = ({ ["description"] : ("Check if server is reachable at "+getBackendURL(env.EVENT).href), ["closeButton"] : true, ["duration"] : 120000, ["id"] : "websocket-error" });
  const [userDismissed, setUserDismissed] = useState(false);
  (useEffect(
() => {
    if ((connectErrors.length >= 2)) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}
, [connectErrors]))

  return (
    <Toaster closeButton={false} expand={true} position={"bottom-right"} richColors={true} theme={resolvedColorMode}/>
  )
}

export function Link_af00c102e2c2a7018dd100f1a1f1b98d () {



  return (
    <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} target={(true ? "_blank" : "")}>
  <NextLink href={"https://reflex.dev/docs/getting-started/introduction/"} passHref={true}>
  <RadixThemesButton>
  {"Check out our docs!"}
</RadixThemesButton>
</NextLink>
</RadixThemesLink>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Iconbutton_52395c54b68ff5a6f498d43b99daaac3 () {
  const { toggleColorMode } = useContext(ColorModeContext)
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_9922dd3e837b9e087c86a2522c2c93f8 = useCallback(toggleColorMode, [addEvents, Event, toggleColorMode])


  return (
    <RadixThemesIconButton css={({ ["padding"] : "6px", ["position"] : "fixed", ["top"] : "2rem", ["right"] : "2rem", ["background"] : "transparent", ["color"] : "inherit", ["zIndex"] : "20", ["&:hover"] : ({ ["cursor"] : "pointer" }) })} onClick={on_click_9922dd3e837b9e087c86a2522c2c93f8}>
  <Fragment_eb4ad804ee463e78d3c73fc2a2903123/>
</RadixThemesIconButton>
  )
}

export function Fragment_e521b13e556da291bcec5187a783ea81 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue((connectErrors.length > 0)) ? (
  <Fragment>
  <LucideWifiOffIcon css={({ ["color"] : "crimson", ["zIndex"] : 9999, ["position"] : "fixed", ["bottom"] : "33px", ["right"] : "33px", ["animation"] : (pulse+" 1s infinite") })} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Div_24a2e81d0c5d3cb5b5f786fdef44e514 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>
  <Fragment_e521b13e556da291bcec5187a783ea81/>
</div>
  )
}

export function Fragment_eb4ad804ee463e78d3c73fc2a2903123 () {
  const { resolvedColorMode } = useContext(ColorModeContext)



  return (
    <Fragment>
  {isTrue((resolvedColorMode === "light")) ? (
  <Fragment>
  <LucideSunIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
) : (
  <Fragment>
  <LucideMoonIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
)}
</Fragment>
  )
}

export function Link_3607b2ee649d0f223249459744b7335b () {
  const { resolvedColorMode } = useContext(ColorModeContext)



  return (
    <RadixThemesLink asChild={true} css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} size={"3"}>
  <NextLink href={"https://reflex.dev"} passHref={true}>
  <RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["textAlign"] : "center", ["padding"] : "1em" })} direction={"row"} gap={"3"}>
  {"Built with "}
  <svg css={({ ["viewBox"] : "0 0 56 12", ["fill"] : "none" })} height={"12"} width={"56"} xmlns={"http://www.w3.org/2000/svg"}>
  <path css={({ ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") })} d={"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"}/>
  <path css={({ ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") })} d={"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"}/>
  <path css={({ ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") })} d={"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"}/>
  <path css={({ ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") })} d={"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"}/>
  <path css={({ ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") })} d={"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"}/>
  <path css={({ ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") })} d={"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"}/>
</svg>
</RadixThemesFlex>
</NextLink>
</RadixThemesLink>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment>
  <Div_24a2e81d0c5d3cb5b5f786fdef44e514/>
  <Toaster_9d6e054b03c6e5d1bea1c0a5576b4e6d/>
</Fragment>
  <RadixThemesContainer css={({ ["padding"] : "16px" })} size={"3"}>
  <Iconbutton_52395c54b68ff5a6f498d43b99daaac3/>
  <RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["minHeight"] : "85vh" })} direction={"column"} justify={"center"} gap={"5"}>
  <RadixThemesHeading size={"9"}>
  {"Welcome to Reflex!"}
</RadixThemesHeading>
  <RadixThemesText as={"p"} size={"5"}>
  {"Get started by editing "}
  <RadixThemesCode>
  {"CalHacks2024/CalHacks2024.py"}
</RadixThemesCode>
</RadixThemesText>
  <Link_af00c102e2c2a7018dd100f1a1f1b98d/>
</RadixThemesFlex>
  <RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%" })}>
  <Link_3607b2ee649d0f223249459744b7335b/>
</RadixThemesFlex>
</RadixThemesContainer>
  <NextHead>
  <title>
  {"Calhacks2024 | Index"}
</title>
  <meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
