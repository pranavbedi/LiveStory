import React, { useState, useRef } from 'react';
import Lottie from "lottie-react";
import first_pig_talking from "./lottie-animations/first-pig-talking.json";
import first_pig_thinking from "./lottie-animations/first-pig-thinking.json";
import Vapi from "@vapi-ai/web";

function characterComponent() {
  const [onCall, setCallState] = useState(false);
  const vapiKey = "ca83ff8e-21f7-47b2-8f81-c7812d203ad7";
  const assistantKey = 'f9cd08ce-38a0-4809-b666-10d4c6254f9d'; // Replace with your actual assistant key
  const vapiRef = useRef(null);

  // Initialize Vapi instance only once
  if (vapiRef.current === null) {
    vapiRef.current = new Vapi(vapiKey);
  }

  async function toggleCall() {
    if (onCall) {
      // Stop the call
      vapiRef.current.stop();
    } else {
      // Start the call
      await vapiRef.current.start(assistantKey);
    }
    // Toggle the call state
    setCallState(!onCall);
  }

  return (
    <div>
      <div onClick={toggleCall} style={{ cursor: 'pointer', width: '300px', margin: '0 auto' }}>
        <Lottie
          animationData={onCall ? first_pig_talking : first_pig_thinking}
          loop={true}
          style={{ width: '100%', height: 'auto' }}
        />
      </div>
    </div>
  );
}

export default characterComponent;


