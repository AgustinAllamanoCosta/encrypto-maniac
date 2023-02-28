import { Controller,Get, Body, Post } from '@nestjs/common';
import { UserChallengeDto } from '../models/user.challenge.dto';
import { UserPublicKeyDto } from '../models/user.public.key.dto';
import { AuthService } from './auth.service';

@Controller('auth')
export class AuthController {

    constructor(private readonly service: AuthService){}

    @Post('/user/add')
    addUser(@Body() publicKey: UserPublicKeyDto) {
        this.service.addUserPublicKey(publicKey);
    }

    @Get('/user/login')
    siginUser(@Body() userChalleng: UserChallengeDto) {
        return this.service.singInUser(userChalleng);
    }

}
