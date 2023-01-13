import { NextPage } from "next"
import { useEffect, useState } from "react"
import { LoginHome } from "@/components/user"
import { json } from "stream/consumers"
import {User} from '@/modules/types'
interface Props{ article: string }

const LoginHomePage: NextPage<Props> = ({docs}: any) => {
    const [loginUser, setLoginUser] = useState("")
    
    useEffect(()=>{
        const json = JSON.stringify(localStorage.getItem("loginUser"))

        
        setLoginUser(json)
    },[])
    type loginUser = typeof loginUser;
    return (<><div>로그인 정보 : {loginUser} </div></>)
}
export default LoginHomePage