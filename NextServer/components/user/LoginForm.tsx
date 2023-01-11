import '../styles/Login.css'
import { useDispatch } from 'react-redux';

import { useForm } from "react-hook-form";
import styled from 'styled-components'

export default function LoginForm(){
    const dispatch = useDispatch()
    const { register, handleSubmit, formState: { errors } } = useForm();

    return (
        <><h1>로그인</h1>
        <form action="/send-data-here" method="post">
          <label htmlFor="first">User Email:</label>
          <input type="text" id="user_email" name="user_email" />
          <label htmlFor="last">Password:</label>
          <input type="text" id="password" name="password" />
          <button type="submit">Submit</button>
        </form>        
        
        </>
 );
}