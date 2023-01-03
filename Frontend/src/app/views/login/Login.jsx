import React from "react";
import FormularioDeLogin from "../../components/formulario-de-login/FormularioDeLogin";

const Login = (props) => {
    return (
        <FormularioDeLogin setIsLogged={props.setIsLogged}/>
    );
};

export default Login;