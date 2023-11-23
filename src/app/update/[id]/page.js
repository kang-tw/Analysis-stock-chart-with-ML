"use client";


import { useParams, useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function Update() {
    const [title, setTitle] = useState('');
    const [body,setBody] = useState('');

    const router = useRouter();
    const params = useParams();
    const id = params.id;


    useEffect(()=>{

        fetch("http://localhost:9999/topic/"+id)
        .then(resp=>resp.json())
        .then(result=>{
            setTitle(result.title);
            setBody(result.body);
        });


    },[])


    return(
        <form onSubmit={(event)=>{
            event.preventDefault();
            const title = event.target.title.value;
            const body = event.target.body.value;
            const options = {
                method:'POST',
                headers: {
                    'Content-Type':'application/json'
                },
                body:JSON.stringify({title,body})

            }
            fetch("http://localhost:9999/topic",options).then(res=>res.json()).then(result =>{
                console.log(result);
                const last_id = result.id;
                router.push(`/read/${last_id}`);
                router.refresh();
            })



        }}>

        <p>
            <input type="text" name ="title" placeholder="title" value ={title}/>
        </p>
        <p>
            <textarea name ="body" placeholder="body" value={body}></textarea>
        </p>

        <p>
            <input type="submit" value="create"/>
        </p>

    </form>

)


}