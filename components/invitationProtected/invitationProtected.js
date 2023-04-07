'use client'
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import Countdown from "../../components/countDown/countDown";
import Image from 'next/image'
import Music from "../../components/musicButton/musicButton";

const InvitationProtected = () => {
  const router = useRouter();

  useEffect(() => {
    const authenticated = window.sessionStorage.getItem('authenticated');
    if (!authenticated) {
        router.push('/');
    }
  }, []);

  // Si el usuario está autenticado, mostrar el contenido de la página
  return (
    <div>
      {/* <div>
          <Image src="/utils/foto1.jpg" alt="imagen principal" width={1000} height={300} layout="responsive"/>
      </div> */}
      <div>
      <Countdown
          date={"2023-04-29T15:43:40.237Z"}
      />
      <Music/>
      </div>
    </div>
  );
};

export default InvitationProtected;