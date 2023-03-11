import { Test, TestingModule } from '@nestjs/testing';
import { Repository } from 'typeorm';
import { AuthController } from './auth.controller';
import { AuthService } from './auth.service';
import { UserKey } from './entity/user.keys.entity';

describe('AuthController', () => {
  let controller: AuthController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [AuthController],
      providers: [AuthService]
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

    controller = module.get<AuthController>(AuthController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
