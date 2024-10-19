/**
 * Returns button that toggles between Start and Stop call. Call it with the key of the ASSISTANT, whereas
 * vapiKey is your account's public key.
 */

import Vapi from "@vapi-ai/web";
import { useState } from "react";

const vapiKey = "<vapiKey>";
const vapi = new Vapi(vapiKey);

export function StartCallButton({ assistantKey }) {
  const [onCall, setCallState] = useState(false);

  async function togglePhone() {
    console.log("Toggle call with assistantKey:", assistantKey);
    onCall ? vapi.stop() : await vapi.start(assistantKey);
    setCallState(!onCall);
  }

  return (
    <button onClick={() => togglePhone()}>
      {onCall ? "Stop Call" : "Start Call"}
    </button>
  )
};