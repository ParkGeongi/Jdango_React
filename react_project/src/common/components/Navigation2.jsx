import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';

import { Link } from "react-router-dom"

const Navigation2 = () => {
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ width: 800 }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        <Link to="/home" style={{width:35, margin:10}}>Home</Link>
        <Link to="/counter" style={{width:50, margin:10}}>Counter</Link>
        <Link to="/todos" style={{width:35, margin:10}}>Todos</Link>
        <Link to="/signup" style={{width:95, margin:10}}>Blog Sign up</Link>
        <Link to="/login" style={{width:40, margin:10}}>Login</Link>
        <Link to="/stroke" style={{width:40, margin:10}}>Stroke</Link>
        <Link to="/iris" style={{width:20, margin:10}}>Iris</Link>
        <Link to="/fashion" style={{width:50, margin:10}}>Fashion</Link>
        <Link to="/number" style={{width:50, margin:10}}>Number</Link>
        <Link to="/navermoives" style={{width:90, margin:10}}>Naver_Movies</Link>
        <Link to="/samsung" style={{width:50, margin:10}}>Samsung</Link>
      </BottomNavigation>
    </Box>
  );
}

export default Navigation2