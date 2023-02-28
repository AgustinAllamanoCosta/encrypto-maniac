import { Injectable } from '@nestjs/common';
import { UserChallengeDto } from '../models/user.challenge.dto';
import { UserPublicKeyDto } from '../models/user.public.key.dto';
import { AuthRepository } from './auth.repository';

@Injectable()
export class AuthService {

    constructor(private readonly repository: AuthRepository){}

    public singInUser(userChalleng: UserChallengeDto) {
        throw new Error('Method not implemented.');
    }

    public addUserPublicKey(publicKey: UserPublicKeyDto) {
        throw new Error('Method not implemented.');
    }
}
