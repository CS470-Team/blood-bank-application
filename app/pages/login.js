import { Typography, CssBaseline, Box, TextField, FormControlLabel, Checkbox, Button, Grid, Link, Alert } from "@mui/material";
import axios from "axios";
import Layout from "../components/layout";
import { useState } from "react";

function Copyright(props) {
    return (
      <Typography variant="body2" color="text.secondary" align="center" {...props}>
        {'Copyright © '}
        <Link color="inherit" href="https://mui.com/">
          Your Website
        </Link>{' '}
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    );
  }

export default function Login() {
    const [error, setError] = useState(null);
    const handleSubmit = (event) => {
        event.preventDefault();
        const form = event.target;
        
        const data = {
            email: form.email.value,
            password: form.password.value
        }

        axios({
            method: "post",
            url: "/api/login",
            data: data,
            headers: { "Content-Type": "application/json" }
        }).then(res => {
            if (res.status === 200) {
                window.location.href = "/";
            }
        }).catch(err => {
            setError(err.response.data.message);
        });
        
    };
    
    return (
        <Layout>
            <CssBaseline />
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Email Address"
                        name="email"
                        autoComplete="email"
                        autoFocus
                    />
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        autoComplete="current-password"
                    />
                    <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Remember me"
                    />
                    { error && 
                        <Alert severity="error">
                            {error}
                        </Alert>
                    }
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                    >
                        Sign In
                    </Button>
                    <Grid container>
                        <Grid item xs>
                            <Link href="#" variant="body2">
                                Forgot password?
                            </Link>
                        </Grid>
                        <Grid item>
                            <Link href="#" variant="body2">
                                {"Don't have an account? Sign Up"}
                            </Link>
                        </Grid>
                    </Grid>
                </Box>
            </Box>
            <Copyright sx={{ mt: 8, mb: 4 }} />
        </Layout>
    );
}