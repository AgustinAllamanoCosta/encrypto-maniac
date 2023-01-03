import React, { useState } from "react";

const App = () => {
    const [isLogged, setIsLogged] = useState(false);

    if (isLogged) {
        return (<></>);
    } else {
        return (
            <>
                <Login setIsLogged={setIsLogged} />
            </>
        );
    }
};

export default App;