"use client";

import { useRouter } from "next/navigation";
import { useState, useEffect } from "react";
import styles from "./formLogin.module.css";
import { encryptName, Match, createToast } from "../usefulFunctions/usefulFunctions";
import axios from "axios";

const guestForm = {
  name: "",
  code: "",
};

const FormLogin = () => {

  const port = process.env.NEXT_PUBLIC_PORT;

  const router = useRouter();

  const [form, setForm] = useState(guestForm);
  const [allGuests, setAllGuest] = useState([]);
  const [showPassword, setShowPassword] = useState(false);

  const getGuests = async () => {
    await axios
      .get(`${port}guest/all`)
      .then((response) => {
        setAllGuest(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    getGuests();
  }, []);

  const handleChange = (e) => {
    e.preventDefault();
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if(form.name==="Giovana Mendez" && form.code==="xvgiovaM"){
      router.push("/createGuests");
      createToast("success", "Bienvenida Giova, ya puedes cargar todos tus invitados")
    }
    else if (Match(allGuests, form.code)) {
      window.sessionStorage.setItem("authenticated", true);
      router.push("/invitation");
      createToast("success", "Bienvenido " + form.name)
    } else {
      createToast("error", "Código incorrecto");
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Login</h1>
      <form onSubmit={handleSubmit}>
        <label className={styles.label}>
          Nombre:
          <input
            type="text"
            className={styles.input}
            name="name"
            value={form.name}
            onChange={handleChange}
          />
        </label>
        <label className={styles.label}>
          Código:
          <div className={styles.passwordContainer}>
            <input
              type={showPassword ? "text" : "password"}
              className={styles.input}
              name="code"
              value={form.code}
              onChange={handleChange}
            />
            <button
              type="button"
              className={styles.showPasswordButton}
              onClick={() => setShowPassword(!showPassword)}
            >
              {showPassword ? "🐵" : "🙈"}
            </button>
          </div>
        </label>
        <button type="submit" className={styles.submitButton}>
          Ingresar
        </button>
      </form>
    </div>
  );
};

export default FormLogin;
