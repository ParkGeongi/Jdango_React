import { NextPage } from "next"
import { useState, useEffect } from "react"
import { LoginHome } from "@/components/user"

interface Props{ user: string }

const LoginHomePage: NextPage<Props> = () => {
    const [email, setEmail] = useState("")
    useEffect(() => {
      setEmail(JSON.stringify(localStorage.getItem("email")))
      },[]);

    return (<LoginHome email={email} />)
}
export default LoginHomePage