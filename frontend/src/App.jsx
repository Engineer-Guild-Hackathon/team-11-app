import { Button, TextField, Container, Typography } from '@mui/material';
import SendIcon from '@mui/icons-material/Send';

function App() {
  return (
    <Container maxWidth="sm" style={{ marginTop: '4rem' }}>
      <Typography variant="h4" component="h1" gutterBottom align="center">
        メンターAI 🤖
      </Typography>
      
      <TextField
        fullWidth
        label="達成したい目標（例: 英検準1級に合格）"
        variant="outlined"
        margin="normal"
      />
      
      <TextField
        fullWidth
        label="現在の立ち位置（例: 英検2級を保持）"
        variant="outlined"
        margin="normal"
      />

      <Button
        variant="contained"
        endIcon={<SendIcon />}
        size="large"
        fullWidth
        style={{ marginTop: '1rem', paddingTop: '0.75rem', paddingBottom: '0.75rem' }}
      >
        ロードマップを生成
      </Button>
    </Container>
  );
}

export default App;