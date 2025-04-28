export const handleLogin = (formFields) => {
  // now you have access to these variables through destructuring
  const { username, password } = formFields;
  console.log(formFields);
};

export const handleSignUp = (formFields) => {
  // now you have access to these variables through destructuring
  const { username, password, email } = formFields;
  console.log(formFields);
};

export const loginWithGoogle = () => {};
