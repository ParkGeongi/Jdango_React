import { Route, Routes } from "react-router-dom"
import { LoginForm } from "auth"

import {Counter, Footer, Navigation2} from "common"
import { Schedule } from "todos"
import dog from '../../images/fashion.png'
import { Number,Fashion, Iris, Stroke} from "ml"
import {NaverMovie } from "webcrawler"
import { BlogSignup } from "blog"
import { Samsung } from "nlp"


const Home = () => {
    const imgsize = {width:500, height: 500}
    return (<>       
    <table style={{ width: "1200px", height: "550px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}>
                <Navigation2/>
           
                
                    </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%",height: "80%",  border: "1px solid black"}}>
        <td style={{ width: "100%", border: "1px solid black"}}>
         <Routes>   
            <Route path="/counter" element={<Counter/>}></Route>
            <Route path="/todos" element={<Schedule/>}></Route>
            <Route path="/login" element={<LoginForm/>}></Route>
            <Route path="/signup" element={<BlogSignup/>}></Route>
            <Route path="/iris" element={<Iris/>}></Route>
            <Route path="/stroke" element={<Stroke/>}></Route>
            <Route path="/fashion" element={<Fashion/>}></Route>
            <Route path="/number" element={<Number/>}></Route>
            <Route path="/navermoives" element={<NaverMovie/>}></Route>
            <Route path="/samsung" element={<Samsung/>}></Route>
        </Routes>
        </td>
        </tr>
        <tr>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <img src = {dog} style={imgsize} alt = 'dog'/>
            </td>
        </tr>
        <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                <Footer/> 
                
            </td>
        </tr>
        </tbody>
    </table>
    </>
    )
}

export default Home