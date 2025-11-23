import { Card, Typography, Box, CardContent, CardMedia, CardActionArea } from "@mui/material";
import React from "react";

interface SignCardProps{
    name?: string,
    meaning?: string, 
    hand_configuration?: string,
    articulation_point?: string,
    movement?: string,
    body_expression?: string,
    direction_and_orientation?: string,
}

const SignCard: React.FC<SignCardProps> = ({ 
    name, 
    meaning, 
    hand_configuration, 
    articulation_point, 
    movement,
    body_expression,
    direction_and_orientation
    }) => {

    return (
        <Card sx={{ maxWidth: 345 }}>
            <CardActionArea>
                <CardMedia
                    component="img"
                    height="140"
                    image="data:image/jpeg;base64,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"
                    alt={name}
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                        {name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {meaning}
                    </Typography>
                    {hand_configuration && (
                        <Typography variant="body2" sx={{ mt: 1 }}>
                            <strong>Hand Configuration:</strong> {hand_configuration}
                        </Typography>
                    )}
                    {articulation_point && (
                        <Typography variant="body2">
                            <strong>Articulation Point:</strong> {articulation_point}
                        </Typography>
                    )}
                    {movement && (
                        <Typography variant="body2">
                            <strong>Movement:</strong> {movement}
                        </Typography>
                    )}
                    {body_expression && (
                        <Typography variant="body2">
                            <strong>Body Expression:</strong> {body_expression}
                        </Typography>
                    )}
                    {direction_and_orientation && (
                        <Typography variant="body2">
                            <strong>Direction and Orientation:</strong> {direction_and_orientation}
                        </Typography>
                    )}
                    {/* Add other properties as needed */}
                </CardContent>
            </CardActionArea>
        </Card>
    );
}

export default SignCard;