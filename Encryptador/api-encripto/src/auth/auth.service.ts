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

    public async addUserPublicKey(publicKey: UserPublicKeyDto) {
        if(this.userRepository.findOneBy({ name: publicKey.name })){
            throw new Error('The key alredy exist in the user');
        }
        const userKey = this.userRepository.create(publicKey);
        const entityInTheDataBase = await this.userRepository.save(userKey);
        return entityInTheDataBase.id;
    }
}
