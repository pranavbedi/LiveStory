import React, { useEffect, useState, useRef } from 'react';
import Lottie from "lottie-react";
import Vapi from "@vapi-ai/web";

const VOICE_AND_ANIMATION_DATA = {
  "transcriber": {
    "provider": "deepgram",
    "model": "nova-2",
    "language": "en-US"
  },
  "model": {
    "provider": "groq",
    "model": "llama3-70b-8192"
  },
  "characters": {
    "first-pig": {
      "provider": "11labs",
      "voiceID": "burt",
      "animations": {
        "talking": "../lottie-animations/first-pig-talking.json",
        "thinking": "../lottie-animations/first-pig-thinking.json"
      },
      "name": "first little pig"
    },
    "second-pig": {
      "provider": "11labs",
      "voiceID": "hH9RoP1FkT4aZf5lPZFz", // Dan Wright, annoying
      "animations": {
        "talking": "../lottie-animations/second-pig-talking.json",
        "thinking": "../lottie-animations/second-pig-thinking.json"
      },
      "name": "second little pig"
    },
    "third-pig": {
      "provider": "11labs",
      "voiceID": "5lm1mr2qVzTTtc8lNLgo", // Ayden from 11labs
      "animations": {
        "talking": "../lottie-animations/third-pig-talking.json",
        "thinking": "../lottie-animations/third-pig-thinking.json"
      },
      "name": "third little pig"
    },
    "wolf": {
      "provider": "11labs",
      "voiceID": "EiNlNiXeDU1pqqOPrYMO",
      "animations": {
        "talking": "../lottie-animations/wolf-talking.json",
        "thinking": "../lottie-animations/wolf-thinking.json"
      },
      "name": "big bad wolf"
    }
  },
  "prompts": {
    "first-pig": `
    You are the First Pig, a scared and wimpy character with a nasally voice.
    You often panic at the slightest sign of danger and tend to overreact. You do not see yourself as smart or strong as your two older brothers.

    Your older brother, the Second Pig is cocky and overconfident.
    Your older brother, the Third Pig, is smart and intelligent.
    `,
    "second-pig": `
    You are the Second Pig, a cocky and confident character.
    You love to show off and believe you are the best at everything. You believe you can handle anything and like saying so.
    Be bold and a little cheeky, always ready to challenge others. You like battering down on your younger brother, the First Pig, and always are trying to prove
    you are better than your older brother, the Third Pig.
    `,
    "third-pig": `
    You are the Third Pig, an intelligent and patient character. You provide wise advice and think carefully before acting. You speak slowly and thoughtfully.
    Your goal is to guide others toward the best solution. You have two younger brothers, who you care very much for and want to help grow into mature, intelligent pigs.
    
    Your youngest brother, the First Pig, is scared and wimpy. He panics often, and you feel responsible for him.
    Your second-youngest brother, the Second Pig, is very cocky and overconfident.
    `,
    "wolf": `
    You are the Big Bad Wolf, a cunning and sly character known for your deceptive charm. 
    You speak with a low, confident voice, often using clever wordplay to manipulate others.
    `,

    "general-formatting": `
    Please respond as the character using simple, clear language.
    Avoid complex words or phrases that might be hard for a child to understand.
    Respond as the character without any stage directions or non-verbal cues. Focus on clear and conversational dialogue that conveys your personality.
    `
  }
}

/**
 * CharacterComponent
 * - Calls backend to access all necessary:
 * 1. Pose
 * 2. Animations when interacting
 * 3. Voice when interacting
 * 4. Context when interacting
 * 
 * Accesses this via a storyID, page (for context), and character.
 */
function CharacterComponent({ storyID, page, character, onTalkingStart, onTalkingEnd }) {
  const [charData, setCharData] = useState(null);
  const [onCall, setCallState] = useState(false);

  const vapiKey = "ca83ff8e-21f7-47b2-8f81-c7812d203ad7";
  const vapiRef = useRef(null);
  const lottieRef = useRef();


  const [isTalking, setIsTalking] = useState(false);
  const [talkingAnimation, setTalkingAnimation] = useState(null);
  const [thinkingAnimation, setThinkingAnimation] = useState(null);
  const [loading, setLoading] = useState(true);


  // Initialize Vapi instance only once
  if (vapiRef.current === null) {
    vapiRef.current = new Vapi(vapiKey);
  }

  useEffect(() => {
    const getAnimationByPath = async (talkingPath, thinkingPath) => {
      setLoading(true);
      try {
        const talking_response = await fetch(talkingPath);
        const thinking_response = await fetch(thinkingPath);
        const talkingData = await talking_response.json();
        const thinkingData = await thinking_response.json();

        setTalkingAnimation(talkingData);
        setThinkingAnimation(thinkingData);
      } catch (error) {
        console.error('Error fetching animations:', error);
      } finally {
        setLoading(false);
      }
    };

    const getPageRelevants = async (page) => {
      try {
        const response = await fetch(`http://localhost:8000/getPages/${page}`);
        const data = await response.json();
        setCharData(data);
      } catch (error) {
        console.error('Error fetching page data:', error);
      }
    }

    getAnimationByPath(
      VOICE_AND_ANIMATION_DATA["characters"][character]["animations"]["talking"],
      VOICE_AND_ANIMATION_DATA["characters"][character]["animations"]["thinking"]
    );
    getPageRelevants(page);

    const handleSpeechStart = () => {
      console.log('Speech has started');
      setIsTalking(true);
      if (onTalkingStart) onTalkingStart();
    };
  
    const handleSpeechEnd = () => {
      console.log('Speech has ended');
      setIsTalking(false);
      if (onTalkingEnd) onTalkingEnd();
    };
    
    // Add listeners
    vapiRef.current.on('speech-start', handleSpeechStart);
    vapiRef.current.on('speech-end', handleSpeechEnd);

    // Cleanup listeners on unmount or when dependencies change
    return () => {
      vapiRef.current.off('speech-start', handleSpeechStart);
      vapiRef.current.off('speech-end', handleSpeechEnd);
    };

  }, [onTalkingStart, onTalkingEnd, page]);

  async function toggleCall() {
    setCallState(!onCall);
    if (onCall) {
      // Stop the call
      vapiRef.current.stop();
    } else {
      // Start the call
      try {
        await vapiRef.current.start({
          transcriber: {
            provider: VOICE_AND_ANIMATION_DATA["transcriber"]["provider"],
            model: VOICE_AND_ANIMATION_DATA["transcriber"]["model"],
            language: VOICE_AND_ANIMATION_DATA["transcriber"]["language"]
          },
          model: {
            provider: VOICE_AND_ANIMATION_DATA["model"]["provider"],
            model: VOICE_AND_ANIMATION_DATA["model"]["model"],
            messages: [
              {
                role: "system",
                content: VOICE_AND_ANIMATION_DATA["prompts"][character] + VOICE_AND_ANIMATION_DATA["prompts"]["general-formatting"] + charData["characters"][character]["messages"]["content"],
              },
            ],
          },
          voice: {
            provider: VOICE_AND_ANIMATION_DATA["characters"][character]["provider"],
            voiceId: VOICE_AND_ANIMATION_DATA["characters"][character]["voiceID"],
          }
        });
      } catch {
        setCallState(!onCall); // set it back
        console.log("Failed to start VapiRef");
      }
    }
  }


  if (loading) {
    return <div>Loading animations...</div>; // Show loading state while fetching
  }
  return (
    <div onClick={toggleCall} style={{ cursor: 'pointer', width: '300px', margin: '0 auto' }}>
      <Lottie
        lottieRef={lottieRef}
        animationData={isTalking ? talkingAnimation : thinkingAnimation}
        loop={true}
        style={{ width: '100%', height: 'auto', display: onCall ? 'block' : 'none' }} // Control visibility with CSS
      />
      {charData && charData.characters[character] && charData.characters[character].poses ? (
        <img 
          src={charData.characters[character].poses[0]} 
          alt="Description of the image" 
          style={{ width: '100%', height: 'auto', display: onCall ? 'none' : 'block' }}
        />
      ) : (
        <div>Loading character image...</div>
      )}
    </div>
  );
}

export default CharacterComponent;