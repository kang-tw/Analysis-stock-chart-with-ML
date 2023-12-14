import styled from "styled-components";

export const Wrapper = styled.div`
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 420px;
    padding: 50px 0px;
`;

export const Title = styled.h1`
    font-size: 42px;
    font-weight: bold; 
`;

export const Form = styled.form`
    margin-top: 50px;
    margin-bottom: 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
`;

export const Input = styled.input`
    outline: none;
    padding: 15px 20px;
    margin: 5px 0px;
    border-radius: 50px;
    border: none;
    width: 100%;
    font-size: 18px;
    &[type="submit"] {
        background-color: #8ca8ba;
        font-family: 'Patua One';
        font-size: 18px;
        color: #FCFCFC;
        cursor: pointer;
        &:hover {
            opacity: 0.8;
        }
    }
`;

export const Error = styled.span`
    color: #F24C3D;
`;

export const Switcher = styled.span`
    margin-top: 20px;
    font-size: 18px;
    a {
        color: #d4c7c7;
        font-weight: 500;
    }
`;