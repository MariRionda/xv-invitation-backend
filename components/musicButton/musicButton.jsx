'use client'
import { useState, useRef, useEffect } from 'react';
import { Howl} from 'howler';

export default function Music() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentPosition, setCurrentPosition] = useState(0); // Estado de la posición actual
  const sound = useRef(null);

  function toggleMusic() {
    setIsPlaying(prev => !prev);

    if (!isPlaying) {
      sound.current = new Howl({
        src: ['/utils/flowers.mp3'],
        onend: function() {
          setIsPlaying(false);
        },
        onload: function() {
          // Si la canción ya se ha reproducido antes, establecer la posición actual
          if (currentPosition > 0) {
            sound.current.seek(currentPosition);
          }
        }
      });
      sound.current.play();
    } else {
      setCurrentPosition(sound.current.seek()); // Guardar la posición actual antes de pausar
      sound.current.pause();
    }
  }

  // Pausar la música si se sale del componente
  useEffect(() => {
    return () => {
      if (sound.current) {
        sound.current.pause();
      }
    };
  }, []);

  return (
    <div>
      <button onClick={toggleMusic}>
        {isPlaying ? '🔊' : '🔈'}
      </button>
    </div>
  );
}
