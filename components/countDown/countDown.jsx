'use client'
import React, { useState, useEffect } from "react";

const Countdown = ({ date }) => {
  const [days, setDays] = useState(0);
  const [hours, setHours] = useState(0);
  const [minutes, setMinutes] = useState(0);
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      const time = Date.parse(date) - Date.parse(new Date());
      setDays(Math.floor(time / (1000 * 60 * 60 * 24)));
      setHours(Math.floor((time / (1000 * 60 * 60)) % 24));
      setMinutes(Math.floor((time / 1000 / 60) % 60));
      setSeconds(Math.floor((time / 1000) % 60));
    }, 1000);

    return () => clearInterval(interval);
  }, [date]);

  return (
    <div style={{display:"flex", justifyContent:"space-between", width:"100%", padding:"60px"}}>
      <div style={{display:"flex", flexDirection: "column", alignItems: "center"}}>
        <div>{days}</div>
        <div>días</div>
      </div>
      <div style={{display:"flex", flexDirection: "column", alignItems: "center"}}>
        <div>{hours}</div>
        <div>hs</div>
      </div>
      <div style={{display:"flex", flexDirection: "column", alignItems: "center"}}>
        <div>{minutes}</div>
        <div>min</div>
      </div>
      <div style={{display:"flex", flexDirection: "column", alignItems: "center"}}>
        <div>{seconds}</div>
        <div>seg</div>
      </div>
    </div>
  );
};

export default Countdown;