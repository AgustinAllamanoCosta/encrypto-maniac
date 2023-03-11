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
      if (token === 'UserKeyRepository') {
        return { 
          create: jest.fn(),
          save: jest.fn(),
          findOneBy: jest.fn()
        };
      }
    })
    .compile();

    service = module.get<AuthService>(AuthService);
    repository = module.get('UserKeyRepository');
  });

  afterAll(()=>{jest.clearAllMocks();});

  it('should be defined', () => {
    expect(service).toBeDefined();
  });

  describe('given a user want to add a public key',()=>{
    const publicKey: UserPublicKeyDto = {
      name: 'userName',
      key: 'some.rsa.public.key'
    };
    it('when the key dosen`t exit, should add the key in the base and return the ID 321', async () => {

      const EXPECTED_DOCUMENT_ID = 321;

      repository.create.mockReturnValue(publicKey);
      repository.save.mockReturnValue({id: EXPECTED_DOCUMENT_ID, ...publicKey});

      const idFromService = await service.addUserPublicKey(publicKey);

      expect(repository.save).toBeCalled();
      expect(repository.create).toBeCalled();
      expect(idFromService).toBe(EXPECTED_DOCUMENT_ID);
    });

    it('when the key dose exit, should throw an error "KeyAlredyInTheDataBase"', async () => {

      repository.findOneBy.mockReturnValue(publicKey);
      const DOCUMENT_ID = 321;
      repository.create.mockReturnValue(publicKey);
      repository.save.mockReturnValue({id: DOCUMENT_ID, ...publicKey});

      const ERROR_MESAGE = 'The key alredy exist in the user';

      await expect(service.addUserPublicKey(publicKey)).rejects.toThrow(ERROR_MESAGE);  

      expect(repository.findOneBy).toBeCalled();
    });
  });
});