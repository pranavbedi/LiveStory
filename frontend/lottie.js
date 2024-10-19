import Lottie from "lottie-react";
import animation from "./lottie-animations/pig-wheel.json";
import first_pig_talking from "./lottie-animations/first-pig-talking.json";
import first_pig_thinking from "./lottie-animations/first-pig-thinking.json";

// EXAMPLE FOR LOADING LOTTIE ANIMS, RETURNS AS REACT COMPONENT

const Example = () => {
    return <div>
        <h3>Pig Wheel</h3>
        <Lottie animationData={animation} />;
        <h3>First Pig</h3>
        <Lottie animationData={first_pig_talking} />;
        <Lottie animationData={first_pig_thinking} />;
    </div>
    
};
  
export default Example