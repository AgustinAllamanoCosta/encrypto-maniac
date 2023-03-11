import { Test, TestingModule } from '@nestjs/testing';
import { UserPublicKeyDto } from '../models/user.public.key.dto';
import { AuthService } from './auth.service';
import { Repository } from 'typeorm';
import { UserKey } from './entity/user.keys.entity';

describe('AuthService', () => {
  let service: AuthService;
  let repository;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [AuthService],
    })
    .useMocker((token) => {
      const results = 'some.mongo.id';
      if (token === 'UserKeyRepository') {
        return { 
          create: jest.fn().mockResolvedValue({ }),
          save: jest.fn().mockResolvedValue(results)
        };
      }
    })
    .compile();

    service = module.get<AuthService>(AuthService);
    repository = module.get('UserKeyRepository');
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });

  describe('given a user want to add a public key',()=>{
    const publicKey: UserPublicKeyDto = {
      name: 'userName',
      key: 'some.rsa.public.key'
    };
    it('when the key dosen`t exit, should add the key in the base', () => {

      service.addUserPublicKey(publicKey);
      expect(repository.save).toBeCalled();
      expect(repository.create).toBeCalled();
    });
  });
});
