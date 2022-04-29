import { Container, Typography } from "@mui/material";

export default function Layout({ title, children }) {
    return (
        <Container>
            <Typography variant="h1">
                { title }
            </Typography>
            { children }
        </Container>
    );
}