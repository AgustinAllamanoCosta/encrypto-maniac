import React from "react";
import { Container, Col, Row, Image, Button, Form } from 'react-bootstrap';
import Logo from "../../img/logo-encrypto-maniac.png";
import Styles from './FormularioDeLogin.module.css';

const FormularioDeLogin = () => {

    return (
        <Form className={Styles.formulario}>
            <Container className={Styles.contenedor}>
                <Image className={Styles.logo} src={Logo} as={Col} />
                <Form.Group className={Styles.input}>
                    <Form.Label> Usuario </Form.Label>
                    <Form.Control className={Styles.textInput} type='text' placeholder='Ingresar usuario...' />
                </Form.Group>
                <Form.Group className={Styles.input}>
                    <Form.Label> Contraseña </Form.Label>
                    <Form.Control className={Styles.textInput} type='password' placeholder='Ingresar contraseña...' />
                </Form.Group>
                <Row className={Styles.rowBoton}>
                    <Button className={Styles.boton} variant='dark' type='submit'> Iniciar </Button>
                </Row>
            </Container>
        </Form>
    );
};

export default FormularioDeLogin;