import { useState } from "react";
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase";
import { Link, useNavigate } from "react-router-dom";
import { Wrapper, Title, Form, Input, Error, Switcher } from "../components/auth-components";

export default function LogIn() {
    const navigate = useNavigate();
    const [isLoading, setLoading] = useState(false);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const onChange = (e) => {
        const { target: { name, value } } = e;
        if (name === "email") {
            setEmail(value)
        } else if (name === "password") {
            setPassword(value)
        }
    };
    const onSubmit = async (e) => {
        e.preventDefault();
        setError("");
        if(isLoading || email === "" || password === "") return;
        try {
            setLoading(true);
            await signInWithEmailAndPassword(
                auth, 
                email, 
                password
            );
            // access to deep
            location.replace("http://223.194.46.169:8080/");
        } catch (e) {
           if(e){
            setError(e.message);
           }
        } finally {
            setLoading(false);
        }
    };
    return (
        <Wrapper>
            <Title>Peek the Future</Title>
            <span>
				Welcome
			</span>
            <Form onSubmit={onSubmit}>
                <Input 
                    onChange={onChange}
                    name="email" 
                    value={email} 
                    placeholder="Email" 
                    type="email" 
                    required
                />
                <Input 
                    onChange={onChange}
                    name="password" 
                    value={password} 
                    placeholder="Password" 
                    type="password" 
                    required
                />
                <Input 
                    type="submit" 
                    value={isLoading ? "Loading..." : "Log in"}
                />
            </Form>
            {error !== "" ? <Error>{error}</Error> : null}
            <Switcher>
                Don't have an account? &nbsp;
                <Link to="/signup">
                    Create one &rarr;
                </Link>
            </Switcher>
        </Wrapper>
    );
};