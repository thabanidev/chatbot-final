import { SignIn } from "@clerk/nextjs";
 
const SignInPage = () => (
  <div className="flex flex-col items-center justify-center h-screen">
    <SignIn />
  </div>
);
export default SignInPage;