import Swal from "sweetalert2";

const bcrypt = require("bcryptjs");


export function encryptName(name) {
  // Generamos un salt (sal) aleatorio
  const salt = bcrypt.genSaltSync(10);
  // Encriptamos el nombre con el salt generado
  const hashedName = bcrypt.hashSync(name, salt);
  // Devolvemos el nombre encriptado
  return hashedName;
}

export function Match(guests, encrypt) {
  let state = false
  guests?.forEach((guest) => {
    if (bcrypt.compareSync(guest.name, encrypt)) {
      state = true
    }
  });
  return state;
}

export const createToast = (icon, title) => {
  const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.addEventListener("mouseenter", Swal.stopTimer);
      toast.addEventListener("mouseleave", Swal.resumeTimer);
    },
  });
  Toast.fire({
    icon,
    title,
  });
};
