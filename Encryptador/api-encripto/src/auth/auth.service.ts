import { Injectable } from '@nestjs/common';
import { UserChallengeDto } from '../models/user.challenge.dto';
import { UserPublicKeyDto } from '../models/user.public.key.dto';
import { Repository } from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';
import { UserKey } from './entity/user.keys.entity';

@Injectable()
export class AuthService {

    constructor(@InjectRepository(UserKey) private userRepository: Repository<UserKey>){}

    public singInUser(userChalleng: UserChallengeDto) {
        throw new Error('Method not implemented.');
    }

    public addUserPublicKey(publicKey: UserPublicKeyDto) {
        const userKey = this.userRepository.create(publicKey);
        return this.userRepository.save(userKey);
    }
}
