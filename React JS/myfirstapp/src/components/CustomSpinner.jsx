import React, { useState, useEffect } from 'react';
import { DNA } from 'react-loader-spinner';

const CustomSpinner = () => {
  const [loading, setLoading] = useState(true);

  // Simulate data fetching
  useEffect(() => {
    setTimeout(() => {
      setLoading(false);
    }, 3000); // Stop loading after 3 seconds
  }, []);

  return (
    <div>
      {loading ? (
        <DNA
          visible={true}
          height="80"
          width="80"
          ariaLabel="dna-loading"
          wrapperStyle={{}}
          wrapperClass="dna-wrapper"
        />
      ) : (
        <h2>Content Loaded!</h2>
      )}
    </div>
  );
};

export default CustomSpinner;
